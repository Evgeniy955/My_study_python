import ast
import datetime
import email.mime.application
import glob
import json
import os
import shutil
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

from Admin_utils.helper_constant_data.helper_constants import tr_icon_image
from App.config.driver_config import ALLURE_REPORT_PATH as APP_REPORT_PATH
from Rest.admin.config import ALLURE_REPORT_PATH as REST_REPORT_PATH
from Rest.admin.config import get_environ
from Testrail_utils.pytest_testrail_api_client.test_rail import TestRail
from Web.config.driver import ALLURE_REPORT_PATH as WEB_REPORT_PATH

PROJECT_CONFIG = get_environ("PROJECT_CONFIG")
RUN_NAME = get_environ("RUN_NAME")
PLATFORM = get_environ("PLATFORM")
PLATFORM_AND_APP = get_environ("PLATFORM_AND_APP")
MAIL_ADDRESS = get_environ("MAIL_ADDRESS")
MAIL_PASSWORD = get_environ("MAIL_PASSWORD")
ENVIRONMENT = get_environ("ENVIRONMENT")
LANGUAGE = get_environ("LANGUAGE")
ALLURE_PATH = {"App": APP_REPORT_PATH, "Rest": REST_REPORT_PATH, "Web": WEB_REPORT_PATH}
CREATE_ALLURE_REPORT = get_environ("CREATE_ALLURE_REPORT")
TEST_MODE = get_environ("TEST_MODE")
SEND_MAIL = get_environ("SEND_MAIL")

ALLURE_CATEGORIES = [
    {"name": "Ignored tests", "matchedStatuses": ["skipped"]},
    {"name": "Infrastructure problems", "matchedStatuses": ["broken", "failed"], "messageRegex": ".*bye-bye.*"},
    {"name": "Outdated tests", "matchedStatuses": ["broken"], "traceRegex": ".*FileNotFoundException.*"},
    {"name": "Failed tests", "matchedStatuses": ["failed"]},
    {
        "name": "Broken tests without correspond TR case",
        "matchedStatuses": ["broken"],
        "messageRegex": ".*Cases without correspond tests in TR.*",
    },
]

TR_PROJECT_ID = {
    "App": os.environ.get("TR_PROJECT_ID_APP", 70),
    "Rest": os.environ.get("TR_PROJECT_ID_REST", 62),
    "Web": os.environ.get("TR_PROJECT_ID_WEB", 67),
    "Sdk": os.environ.get("TR_PROJECT_ID_SDK", 180),
}


class Archive:
    def __init__(self, folder_path):
        self.passed = self.failed = self.total = 0
        self.folder_path = folder_path
        file_name = os.path.join(os.path.dirname(folder_path), "tmp_zip")
        self.zip_file_name = f"{file_name}.zip"
        if os.path.isfile(self.zip_file_name):
            os.remove(self.zip_file_name)
        for file in (
            result for result in os.listdir(folder_path) if result.split(".")[-1] not in ("json", "properties")
        ):
            os.remove(os.path.join(folder_path, file))

        shutil.make_archive(base_name=file_name, root_dir=folder_path, format="zip")
        self.json_files = tuple(
            os.path.join(folder_path, file)
            for file in os.listdir(folder_path)
            if file.split(".")[-1] == "json" and "categories" not in file
        )

    def get_statistic(self):
        names = []
        for file in (json.loads(open(file, "r").read()) for file in self.json_files):
            if file.get("name") not in names:
                status = file.get("status")
                if status == "passed":
                    self.passed += 1
                elif status == "failed":
                    self.failed += 1
                names.append(file["name"])

        self.total = self.passed + self.failed

    def send_mail(self, delete_archive: bool = False):
        self.get_statistic()

        addr_from = MAIL_ADDRESS
        password = MAIL_PASSWORD

        if TEST_MODE:
            addr_to = [
                "email_for@test.com",
            ]
        else:
            addr_to = [
                "3d4m-qa-allure-report-aaaaeqo6443rn7cxhycrmjjz3m@elsevier.org.slack.com",
            ]
        run_name = RUN_NAME if RUN_NAME is not None else ""
        extension = self.zip_file_name.split(".")[-1]
        main_name = (
            f'{PROJECT_CONFIG} {run_name} {PLATFORM} tests results on {datetime.datetime.today().strftime("%d.%m.%Y")}'
        )
        with open(self.zip_file_name, "rb") as file:
            file_to_send = email.mime.application.MIMEApplication(file.read())
            file_to_send.add_header("Content-Disposition", "attachment", filename=f"{main_name}.{extension}")
        if "App" in PROJECT_CONFIG:
            body = (
                f"{PLATFORM}, executed {self.total} tests\n"
                f"Total passed - {self.passed}\n"
                f"Total failed - {self.failed}"
            )
        elif "Web" in PROJECT_CONFIG:
            body = (
                f"Executed on {LANGUAGE}, {ENVIRONMENT} - {self.total} tests\n"
                f"Total passed - {self.passed}\n"
                f"Total failed - {self.failed}"
            )
        elif "Rest" in PROJECT_CONFIG:
            body = f"Executed {self.total} tests\n" f"Total passed - {self.passed}\n" f"Total failed - {self.failed}"
            args = sys.argv
            if "-m" in args:
                body += f'\n\nMarks: {args[args.index("-m") + 1]}'

        with SMTP("smtp.office365.com", 587) as server:
            server.starttls()
            server.login(addr_from, password)
            msg = MIMEMultipart()
            msg["From"] = addr_from
            msg["To"] = ", ".join(addr_to)
            msg["Subject"] = main_name

            msg.attach(MIMEText(body, "plain"))
            msg.attach(file_to_send)

            server.send_message(msg)

        if delete_archive:
            os.remove(self.zip_file_name)


def get_cases_names_from_allure(report_path):
    list_of_cases_names = []
    for file in glob.glob(os.path.join(report_path, "*.json")):
        with open(file, encoding="utf-8", mode="r") as test_case:
            test_case_dict = dict(json.load(test_case))
            if "parameters" in test_case_dict.keys():
                parameters = ast.literal_eval(test_case_dict["parameters"][0]["value"])
                case_name = test_case_dict["name"]
                for key, value in parameters.items():
                    key = f"<{key}>"
                    case_name = case_name.replace(key, value)
                parameters_in_case_name = "[" + case_name.split("[")[-1]
                case_name = case_name.replace(parameters_in_case_name, "")
            else:
                case_name = test_case_dict["name"]
            if "BUG" in case_name:
                case_name = case_name.split(":")[1]
            case_name = case_name.strip()
            list_of_cases_names.append({"tr_case_name": case_name, "original_allure_case_name": test_case_dict["name"]})
    return list_of_cases_names


def set_tr_links_for_allure_cases(list_of_cases_names, tr_cases, report_path):
    for case in list_of_cases_names:
        case["case_id"] = next(
            (tr_case.id for tr_case in tr_cases if tr_case.title == case["tr_case_name"]),
            "Case name is not found in TR base, please review",
        )
    unique_cases = [dict(case_tuple) for case_tuple in {tuple(case.items()) for case in list_of_cases_names}]
    for file in glob.glob(os.path.join(report_path, "*.json")):
        with open(file, encoding="utf-8", mode="r") as test_case:
            test_case_dict = dict(json.load(test_case))
        for case in unique_cases:
            if test_case_dict["name"] == case["original_allure_case_name"]:
                link = (
                    ""
                    if "not found" in str(case["case_id"])
                    else f"https://3d4medical.testrail.net/index.php?/cases/view/{str(case['case_id'])}"
                )

                link_text = case["case_id"] if "not found" in str(case["case_id"]) else "Link to TR case"
                link_style = "color:red;" if "not found" in str(case["case_id"]) else ""
                final_link = f"<a style='{link_style}' href ='{link}' target='_blank'>{link_text}</a>"
                tr_icon = (
                    f'<img style="display: inline-block;vertical-align: middle;" width="40px" height="40px" '
                    f'src="data:image/svg+xml;base64,{tr_icon_image}">'
                )
                description_html = (
                    test_case_dict["descriptionHtml"] if "descriptionHtml" in test_case_dict.keys() else ""
                )
                test_case_dict["descriptionHtml"] = f"{description_html}<br>{final_link}{tr_icon}"

                if "not found" in str(case["case_id"]):
                    if test_case_dict["status"] == "passed":
                        test_case_dict["statusDetails"] = {"message": "Cases without correspond tests in TR"}
                    else:
                        test_case_dict["statusDetails"] = {
                            "message": f"{test_case_dict['statusDetails']['message']}"
                            f"Cases without correspond tests in TR"
                        }
                    test_case_dict["status"] = "broken"

        with open(file, encoding="utf-8", mode="w") as test_case:
            json.dump(test_case_dict, test_case)


def prepare_allure_results(report_path):
    tr_cases = TestRail().cases.get_cases(project_id=20, suite_id=TR_PROJECT_ID[PROJECT_CONFIG])
    list_of_cases_names = get_cases_names_from_allure(report_path)
    set_tr_links_for_allure_cases(list_of_cases_names, tr_cases, report_path)


def send_mail():
    if CREATE_ALLURE_REPORT and SEND_MAIL:
        report_path = (
            os.path.join(f"{ALLURE_PATH[PROJECT_CONFIG]}/allure-results", f"{PLATFORM.lower()}")
            if PROJECT_CONFIG == "App"
            else os.path.join(f"{ALLURE_PATH[PROJECT_CONFIG]}", "allure-results")
        )
        prepare_allure_results(report_path)
        if PROJECT_CONFIG == "App":
            env_variables = {
                "PLATFORM": PLATFORM,
                "PLATFORM_AND_APP": PLATFORM_AND_APP,
            }
            with open(f"{report_path}/environment.properties", "w") as env_file:
                env_file.write("\n".join(f"{key}={value}" for key, value in env_variables.items()))

        with open(f"{report_path}/categories.json", "w") as allure_categories:
            json.dump(ALLURE_CATEGORIES, allure_categories)
        Archive(report_path).send_mail(delete_archive=True)
        print("Report sent")


if __name__ == "__main__":
    send_mail()
