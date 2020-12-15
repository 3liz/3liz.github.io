github-pages:
	@docker run --rm -w /plugin -v $(shell pwd):/plugin 3liz/pymarkdown:latest tutorial/filezilla.md tutorial/filezilla.html
	@docker run --rm -w /plugin -v $(shell pwd):/plugin 3liz/pymarkdown:latest workshop/qgis_fr_2020.md workshop/qgis_fr_2020.html
