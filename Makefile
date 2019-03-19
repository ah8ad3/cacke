# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

m messages:
	@python manage.localy.py makemessages -l fa

c compile:
	@python manage.localy.py compilemessages

r run:
	@python manage.localy.py runserver

f freeze:
	@pip freeze > requirement.txt

mi migrate:
	@python manage.localy.py migrate

test:
	@python manage.localy.py test
	@python manage.pro.py test

celery:
	@celery -A cacke worker -l info

coverage:
	@coverage run --source='.' manage.localy.py test
	@coverage report
