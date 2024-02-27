think: ## commit the slipbox with :brain: commit
	git commit -m ":brain:" -- slipbox

serve: ## start dev build of site
	HUGO_MODULE_REPLACEMENTS="github.com/daylinmorgan/brain-stem -> brain-stem" \
		hugo -s hugo serve

dev-build: ## build with local theme
	HUGO_MODULE_REPLACEMENTS="github.com/daylinmorgan/brain-stem -> brain-stem" \
		hugo -s hugo


-include .task.cfg.mk .task.mk
$(if $(filter help,$(MAKECMDGOALS)),$(if $(wildcard .task.mk),,.task.mk: ; curl -fsSL https://raw.githubusercontent.com/daylinmorgan/task.mk/v23.1.1/task.mk -o .task.mk))
