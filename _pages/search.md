---
layout: page
permalink: /search/
title: search
description: quick search
nav: false
nav_order: 7
---

<link href="/pagefind/pagefind-ui.css" rel="stylesheet">
<link href="/assets/css/main.css" rel="stylesheet">
<script src="/pagefind/pagefind-ui.js"></script>
<div id="search"></div>
<script>
    window.addEventListener('DOMContentLoaded', (event) => {
        new PagefindUI({ element: "#search", showSubResults: true });
    });
</script>
