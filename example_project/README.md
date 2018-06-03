# Example Project

This is an example project used in the tests for both covered-client and covered-server. The tests require that coverage has been run for this project.

To generate a coverage report, run the following *from this directory*:

```
pytest . --cov=.
```

See `.drone.yml` for an example of how this is done in Drone.
