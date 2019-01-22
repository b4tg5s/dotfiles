# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# Always restore open sites when qutebrowser is reopened.
# Type: Bool
c.auto_save.session = True

# bookmarks
config.bind('a', 'set-cmd-text -s :bookmark-add {url}')
config.bind('A', 'bookmark-add -t')
config.bind('b', 'set-cmd-text -s :bookmark-load')
config.bind('B', 'set-cmd-text -s :bookmark-load -t')

# Message timeout
c.messages.timeout = 6000

# Tabs 
c.fonts.tabs = '12'
c.tabs.background = True
c.tabs.padding = {'top': 1, 'bottom': 2, 'left': 5, 'right': 5}

c.tabs.last_close = 'blank'

# Zoom
c.zoom.default = '125'

# Search engines
c.url.searchengines = {
    "DEFAULT" : "https://www.google.com/search?hl=de&q={}",
    "ddg" : "https://duckduckgo.com/?q={}",
    "maps" : "https://www.openstreetmap.org/search?query={}",
    "gmaps" : "http://maps.google.com/?q={}",
}

#
c.scrolling.bar = "always"

## Keybinding
# new tab is opened next to current tab
config.bind("O", "set-cmd-text -s :open -rt")
