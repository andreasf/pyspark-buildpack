# Cloud Foundry PySpark Buildpack
[![CF Slack](https://www.google.com/s2/favicons?domain=www.slack.com) Join us on Slack](http://slack.cloudfoundry.org)

A Cloud Foundry [buildpack](http://docs.cloudfoundry.org/buildpacks/) for PySpark based apps.

This is based on the [Python buildpack] (https://github.com/cloudfoundry/python-buildpack), which in turn is based on the [Heroku buildpack] (https://github.com/heroku/heroku-buildpack-python).

This buildpack supports running PySpark, Django and Flask apps.

## Buildpack User Documentation

The official Python buildpack documentation can be found at http://docs.cloudfoundry.org/buildpacks/python/index.html.

### PySpark buildpack options

The buildpack allows choosing [OpenJDK] (http://download.pivotal.io.s3.amazonaws.com/openjdk/trusty/x86_64/index.yml) and [Spark] (http://spark.apache.org/downloads.html) versions, as well as disabling caching. Caching is beneficial for staging time, but adds to the staging disk size, which then might exceed the limit (`dea_next.staging_disk_limit_mb`).

The settings can be configured in a file called `spark_runtime.txt` in your application root folder. The available options and defaults are:

```bash
JDK_URL=https://java-buildpack.cloudfoundry.org/openjdk/trusty/x86_64/openjdk-1.8.0_91.tar.gz
JDK_FILENAME=openjdk-1.8.0_91.tar.gz
# Create this checksum on linux with: sha256sum <filename>, 
# and on Mac OS with: shasum -a 256 <filename>.
# The checksum is mandatory and makes sure that the downloaded file is the
# one you expect and not corrupt.
JDK_SHA256=6bc971e0501501bddf61e9095a752a7f00dc27928e3590ff880cc63df081fed3

SPARK_URL=http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz
SPARK_FILENAME=spark-2.1.0-bin-hadoop2.7.tgz
SPARK_SHA256=0834c775f38473f67cb122e0ec21074f800ced50c1ff1b9e37e222a0069dc5c7

# Try setting this to true if you get staging errors
CACHE_DISABLED=false
```

## Building the Buildpack

1. Make sure you have fetched submodules

  ```bash
  git submodule update --init
  ```

1. Get latest buildpack dependencies

  ```shell
  BUNDLE_GEMFILE=cf.Gemfile bundle
  ```

1. Build the buildpack

  ```shell
  BUNDLE_GEMFILE=cf.Gemfile bundle exec buildpack-packager [ --uncached | --cached ]
  ```

1. Use in Cloud Foundry

    Upload the buildpack to your Cloud Foundry and optionally specify it by name

    ```bash
    cf create-buildpack custom_python_buildpack python_buildpack-cached-custom.zip 1
    cf push my_app -b custom_python_buildpack
    ```

## Testing
Buildpacks use the [Machete](https://github.com/cloudfoundry/machete) framework for running integration tests.

To test a buildpack, run the following command from the buildpack's directory:

```
BUNDLE_GEMFILE=cf.Gemfile bundle exec buildpack-build
```

More options can be found on Machete's [Github page.](https://github.com/cloudfoundry/machete)

## Contributing

Find our guidelines [here](./CONTRIBUTING.md).

## Copyright

See [LICENSE](LICENSE) for details.

Copyright (c) 2016 Heroku, Inc.

Copyright (c) 2017 [Dat Tran](http://www.dat-tran.com/), [Andreas Fleig](https://github.com/andreasf).
