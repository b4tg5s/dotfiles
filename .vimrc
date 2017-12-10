""" Move between vim windows
nnoremap <C-H> <C-W><C-H>
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>

""" Split opening to bottom and right
set splitbelow
set splitright

""" Show linenumbers
set nu

""" Colorscheme
colorscheme torte

""" Powerline setup
python3 from powerline.vim import setup as powerline_setup
python3 powerline_setup()
python3 del powerline_setup

""" Powerline config
set laststatus=2 " Display statusline if only one window
set noshowmode " Hide vim's own display of mode
set t_Co=256
