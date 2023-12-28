from zeep import Client

client = Client('http://secure.smartbearsoftware.com/samples/testcomplete10/webservices/Service.asmx?WSDL')
client.transport.session.headers.update({'User-Agent': 'Python Learning Requests'})


def soap():
    sample = client.service.GetSampleObject(3)
    sample['Name'] = "My Test"
    sample['X'], sample['Y'] = sample['Y'], sample['X']
    return sample


def send_soap():
    result = client.service.SetSampleObject(soap())
    return result


if __name__ == "__main__":
    print(send_soap())
