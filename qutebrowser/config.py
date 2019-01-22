# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# Always restore open sites when qutebrowser is reopened.
# Type: Bool
c.auto_save.session = True

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
    "maps" : "http://maps.google.com/?q={}" }

#
c.scrolling.bar = "always"

## Keybinding
# new tab is opened next to current tab
config.bind("O", "set-cmd-text -s :open -rt")
