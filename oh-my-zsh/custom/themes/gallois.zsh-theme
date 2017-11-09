# Depends on the git plugin for work_in_progress()

ZSH_THEME_GIT_PROMPT_PREFIX="%{$reset_color%}%{$fg[green]%}["
ZSH_THEME_GIT_PROMPT_SUFFIX="]%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_DIRTY="%{$fg[red]%}*%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_CLEAN=""

#Customized git status, oh-my-zsh currently does not allow render dirty status before branch
git_custom_status() {
  local cb=$(git_current_branch)
  if [ -n "$cb" ]; then
    echo "$(parse_git_dirty)%{$fg_bold[yellow]%}$(work_in_progress)%{$reset_color%}$ZSH_THEME_GIT_PROMPT_PREFIX$(git_current_branch)$ZSH_THEME_GIT_PROMPT_SUFFIX"
  fi
}

# RVM component of prompt
ZSH_THEME_RVM_PROMPT_PREFIX="%{$fg[red]%}["
ZSH_THEME_RVM_PROMPT_SUFFIX="]%{$reset_color%}"

# vi-mode indicator
VIM_NORMAL="%BNORM%b"
VIM_INSERT="%BINSR%b"

# provide vim mode indicator if vi-mode is active
function _vi_status() {
  if {echo $fpath | grep -q "plugins/vi-mode"}; then
    echo "${${KEYMAP/vicmd/$VIM_NORMAL}/(main|viins)/$VIM_INSERT}"
  fi
}

# Combine it all into a final right-side prompt
RPS1='$(git_custom_status)$(ruby_prompt_info) $EPS1'

PROMPT='%{$fg[cyan]%}[%~% ]%(?.%{$fg[green]%}.%{$fg[red]%}) $(_vi_status) '
