(function () {
    var has_form;

    has_form = document.getElementsByTagName("form").length > 0;
    console.log('Has Form', has_form);

    chrome.extension.onRequest.addListener(function (request, sender, sendResponse) {
        if (request.action == "hasForm") {
            sendResponse({has_form : has_form});
        } else if (request.action == "alert") {
            alert(request.text);
            sendResponse({});
        } else if (request.action == "getText") {
            sendResponse({text : document.body.innerText});
        }
        else {
            console.log(request);
            sendResponse({});
        }
    });

}());
