(function () {

    var storageArea = chrome.storage.local;
    var current_list = null;

    var storage = this.Storage = {
        get : function (key, callback) {
            storageArea.get(key, callback);
        },
        set : function (key, value, callback) {
            storageArea.set({key : value}, callback);
        }
    };

    (function () {
        storage.get("phishing_urls", function (obj) {
            var list = obj['list'];
            if (!list) {
                list = [];
                storage.set("phishing_urls", list, function () {
                    current_list = list;
                });
            } else {
                current_list = list;
            }
        });
    }());

    var inArray = function (list, item) {
        if(!list) {
            return false;
        }
        var i, l = list.length, cur_item;
        for (i = 0; i < l; i += 1) {
            cur_item = list[i];

            if (item == cur_item) {
                return true;
            }
        }
        return false;
    };

    var getList = function () {
      //  console.log(current_list);
        return current_list;
    };

    this.addPhishURL = function (url) {
        var list = getList();
        if (!inArray(list, url)) {
            list.push(url);
            storage.set("phishing_urls", list);
        }
    };

    this.isPhishURL = function (url) {
        var list = getList();
        return inArray(list, url);
    };

}());
