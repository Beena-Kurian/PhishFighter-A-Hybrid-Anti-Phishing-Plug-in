(function (u) {

    function checkForValidUrl(tabId, changeInfo, tab) {
        if (!changeInfo.url) return;
        var url = parse_url(changeInfo.url);
	if (u.check_url(url)) {
            var warningPage = chrome.extension.getURL('blocked/blocked.html?url=' + url.host);
            chrome.tabs.update(tabId, {
                url: warningPage
            });
        }

        chrome.pageAction.show(tabId);
    }
    chrome.tabs.onUpdated.addListener(checkForValidUrl);

    chrome.pageAction.onClicked.addListener(function () {
        chrome.tabs.getSelected(null, function (tab) {
            var tab_id = tab.id;
            var url = parse_url(tab.url).host;

            if (url == "idmsa.apple.com" || url == " www.paypal-media.com" || url == "signin.ebay.com" || url == "pages.ebay.in" || url == "www.paypal.com" || url == "support.apple.com" || url == "store.apple.com" || url == "www.apple.com" || url == "appleid.apple.com" || url == "simple.wikipedia.org" || url == "www.wikipedia.org" || url == "en.wikipedia.org") {
                return;
            }

            var warningPage = chrome.extension.getURL('blocked/blocked.html?url=' + url);

            // Send a request to the content script .
            chrome.tabs.sendRequest(tab.id, {action: "hasForm"}, function (response) {
                var has_form = response.has_form;

                if (!has_form) {
                    console.log('No form found');
                    //chrome.tabs.sendRequest(tab.id, {action : "alert", text : "Continue Browsing"}, function () {
                    //});
                    return;
                }

                chrome.tabs.captureVisibleTab(function (dataUrl) {
                    chrome.tabs.sendRequest(tab.id, {action: "getText"}, function (response) {
                        $.ajax({
                            url: SAVE_URL,
                            method: "post",
                            data: {
                                "file": dataUrl,
                                "url": tab.url,
                                "text": response.text
                            },
                            crossDomain: true,
                            success: function (html) {
                                if (html == "true") {
                                    addPhishURL(url);
                                    chrome.tabs.update(tab_id, {
                                        url: warningPage
                                    });
                                }
                            },
                            error: function () {
                                console.log(arguments);
                            }

                        });
                    });
                });

            });

        });

    });

}(this));
