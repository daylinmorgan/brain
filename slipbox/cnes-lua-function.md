---
title: "Writing a Lua Function"
tags: ["lua","neovim"]
---


In an attempt to improve markdown formatting in the zk cli based zettelkasten
I wanted to build a function atop the zk-nvim plugin in order to take the pick from a telescope/fzf 
then insert the title and link. This feature appears to already be implemented within the zk-lsp.
While I can't guarantee this functionality will suffice at greater complexity it should be fine for now. 
It may be worth pinging the community about how one might achieve this.
What I have written so far seems sufficient albeit incomplete since I have no way of handling file paths. 
It's unclear what the LSP does since it is able to complete. It may be possible to leverage this by surveying the zk-nvim source code. 
If I can achieve this it would simple to implement this feature I think. 

Here is what I had in `~/.config/lvim/lua/commands.lua` at the time of ceasing the endeavor.
The `dump` function was copied from stack overflow for debugging.


```lua
-- custom zk command to drop in a link
local zk = require("zk")
local commands = require("zk.commands")


local function dump(o)
   if type(o) == 'table' then
      local s = '{ '
      for k,v in pairs(o) do
         if type(k) ~= 'number' then k = '"'..k..'"' end
         s = s .. '['..k..'] = ' .. dump(v) .. ','
      end
      return s .. '} '
   else
      return tostring(o)
   end
end


commands.add("ZkLinkTo", function(options)
  zk.pick_notes(options, { title = "ZkLinkTo" }, function(notes)
    local note = notes[1]
    local title = ''
    print(dump(note))
    if note.title then
      title = note.title
    else
      title = "Untitled"
    end
    local link = "[" .. title .. "](".. note.absPath .. ")"
    print(link)
    -- notes = { notes }
    for i, note in ipairs(notes) do
      print(i)
      print(note.title)
      if note.title then
        print("[" .. note.title .. "](".. note.absPath .. ")")
        link = "[" .. note.title .. "](".. note.absPath .. ")"
      else
        print('no title brah')
        link = 'other lin'
        print(link)
      end
      print(link)
      print(note.absPath)
    --   -- vim.cmd("e " .. note.absPath)
    end
  end)
end)
```

[TTY Fonts](o2vi-tty-fonts.md)
