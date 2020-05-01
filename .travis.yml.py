language: python
python:
  - "2.7"
  - "3.4"
  - "3.5"
  - "3.6"      # current default Python on Travis CI
  - "3.7"
  - "3.8"
  - "3.8-dev"  # 3.8 development branch
  - "nightly"  # nightly build
# command to install dependencies
install:
  - pip install -r requirements.txt
# command to run tests
script:
  - python manage.py test