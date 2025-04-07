(function () {
    var blackListedUrls = [
        
        "paypal-com.us.webscrlcmdl.login.submit.dispatch.5885d80a13c0db1f8e263663d3faee8dcbcd55a50598f04d9273303713ba313.emsealtec.com.co",
        "paypal-inc.ml",
        "paypal-kundenverifizierungen.com",
        "paypal-service-update-your-account.com.focaitupeva.com.br",
        "paypal.com-38afd3faeeab644729e759b61614d7b.tripokaridos.com",
        "paypal.com-cgi-bin.dispatch.cmd-home.locale.en-update-account.disrpatch-customer.58741d80a13c0db1f8ea-3b8f5278f9345fwxd452jgb1a50ec1.e831b9a4544152c455hnhb44c83505.belbo.ma",
        "pharmavita.cl",
       
    ];

    this.inBlacklist = function (url) {
        var i, l = blackListedUrls.length, cur_url;
        for (i = 0; i < l; i += 1) {
            cur_url = blackListedUrls[i];
            if (url == cur_url) {
                return true;
            }

            if (url == "www." + cur_url) {
                return true;
            }
        }
        return false;
    };

}());
