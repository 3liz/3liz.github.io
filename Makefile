github-pages:
	@docker run --rm -w /plugin -v $(shell pwd):/plugin 3liz/pymarkdown:latest tutorial/filezilla.md tutorial/filezilla.html
