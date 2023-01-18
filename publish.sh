# install dependencies
pip install wheel, twine

# remove old build
rm -r build dist

# build
python setup.py bdist_wheel

# upload
twine upload dist/*
