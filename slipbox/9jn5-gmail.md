---
title: Gmail
tags:
  - web
  - email
---

Some tips and tricks for myself to use Gmail.

## Gmail Permalink

I have several gmail accounts and the "inbox" url shifts according to the order in which they were authenticated i.e. the `1` in this url shifts:
`https://mail.google.com/mail/u/1/#inbox`.

In order to create stable links (like for a usable bookmark) you need to use a url of the form:

```
https://mail.google.com/mail/u/?authuser=user@gmail.com
```

This link will direct to the correct inbox. Hopefully this option never goes away on Google's end.

## Search

Gmail has a number of [search operators](https://support.google.com/mail/answer/7190?hl=en&ref_topic=3394593&sjid=2040408358466082132-NC)
which can be used to filter emails.

## Managing filters and tags

I make use of the awesome [gmailctl](https://github.com/mbrt/gmailctl) in order to manage all custom filters and tags across my gmail accounts.
This uses `jsonnet` to declaratively configure these filters.

## Managing the inbox through scripts

I use the following script to additionally manage my inbox:

general-archiver.js:

```js
function main() {
  var threads = GmailApp.search(
    '{label:"to be archived"} {label:unread label:inbox} older_than:1d'
  );
  var label = GmailApp.getUserLabelByName("to be archived");

  while (threads.length > 99) {
    // Split the threads array in two
    var littlethreads = threads.splice(0, 99);
    markLabeledAsRead(littlethreads, label);
  }

  markLabeledAsRead(threads, label);
}

function markLabeledAsRead(threads, label) {
  GmailApp.markThreadsRead(threads);
  GmailApp.moveThreadsToArchive(threads);
  threads.map(function (thread) {
    thread.removeLabel(label);
  });
}
```

This means that in concert with the filter setup by gmailctl when an email is tagged with "to be archived"
if I don't read it in a day I'm not likely to read it.
This has been useful for daily newsletters that I'm not likely to read besides the day they arrive.
