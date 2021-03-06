# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# Always restore open sites when qutebrowser is reopened.
# Type: Bool
c.auto_save.session = True

# Bookmarks
config.bind('a', 'set-cmd-text -s :bookmark-add {url}')
config.bind('A', 'bookmark-add -t')
config.bind('b', 'set-cmd-text -s :bookmark-load')
config.bind('B', 'set-cmd-text -s :bookmark-load -t')


c.downloads.location.suggestion = 'both'

# Keys
config.bind("<esc>", "clear-keychain ;; search ;; fullscreen --leave ;; clear-messages")
# new tab next to current tab
config.bind("O", "set-cmd-text -s :open -rt")
# open download
config.bind("<ctrl-o>", "download-open")
# move tabs around
config.bind("<alt-shift-k>", "tab-move -")
config.bind("<alt-shift-j>", "tab-move +")


# Looks
c.scrolling.bar = "always"
c.messages.timeout = 6000
c.zoom.default = '125'


# Search engines
c.url.searchengines = {
    "DEFAULT"   : "https://duckduckgo.com/?q={}",
    "s"     : "https://startpage.com/do/asearch?q={}",
    "g"     : "https://www.google.com/search?hl=de&q={}",
    "d"     : "https://www.duden.de/suchen/dudenonline/{}",
    "maps"  : "https://www.openstreetmap.org/search?query={}",
    "gmaps" : "http://maps.google.com/?q={}",
}


# Tabs 
c.fonts.tabs = '12'
c.tabs.background = True
c.tabs.padding = {'top': 1, 'bottom': 2, 'left': 5, 'right': 5}

c.tabs.last_close = 'blank'
