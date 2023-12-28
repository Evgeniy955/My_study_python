@pytest.fixture(scope="session", autouse=True)
def http_server(request, tmp_path_factory, worker_id, data=None):
    if not worker_id or worker_id == "master":
        # not executing in with multiple workers, just produce the data and let
        # pytest's fixture caching do its job
        server = RedirectionServer()

        def stop():
            server.shutdown()

        request.addfinalizer(stop)
        return server

    # get the temp directory shared by all workers
    root_tmp_dir = tmp_path_factory.getbasetemp().parent

    fn = root_tmp_dir / "data.json"
    with FileLock(str(fn) + ".lock"):
        if fn.is_file():
            data = json.loads(fn.read_text())
        else:
            server = RedirectionServer()
            fn.write_text(json.dumps(data))
    return data