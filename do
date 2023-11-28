#!/usr/bin/env bash

export HUGO_MODULE_REPLACEMENTS="github.com/daylinmorgan/brain-stem -> brain-stem"

function task:serve { : "serve site"
  hugo -s hugo serve
}

function task:build { : "build site"
  hugo -s hugo
}


# ---- do-task boilerplate ---- 
function task:help { : "Show this help"; echo "do:"; w=$(("$(compgen -A function | wc -L)" - 3)); compgen -A function | while read -r name ; do [[ $name =~ ^task: ]] && printf '\033[1;32m%*s\033[0m | %s\n' "$w" "${name#task:}" "$(type "$name" | sed -nEe 's/^[[:space:]]*: ?"(.*)";/\1/p')"; done }
while read -r name; do [[ $name == "task:$1" ]] && shift && "$name" "$@" && exit; done < <(compgen -A function); [[ -n "$1" ]] && printf "\033[1;31m%s\033\0[m is not a task\n" "$1"
task:help # default task
