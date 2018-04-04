app.controller("bankAccountPickOrCreateCtrl", function ($scope, $http, $window, $rootScope) {
    var vm = this;
    vm.url = $rootScope.url;
    vm.accountId = "";
    vm.accounts = [];
    vm.selectBank = "";
    vm.bankChoices = [
        {
            "value": -1,
            "display_name": "Others"
        },
        {
            "value": 0,
            "display_name": "BBL"
        },
        {
            "value": 1,
            "display_name": "Kbank"
        },
        {
            "value": 2,
            "display_name": "Scb"
        },
        {
            "value": 3,
            "display_name": "Ktb"
        },
        {
            "value": 4,
            "display_name": "Tmb"
        },
        {
            "value": 5,
            "display_name": "Krungsri"
        },
        {
            "value": 6,
            "display_name": "Tanachart"
        },
        {
            "value": 7,
            "display_name": "Uob"
        },
        {
            "value": 8,
            "display_name": "Tisco"
        },
        {
            "value": 9,
            "display_name": "Lh"
        },
        {
            "value": 10,
            "display_name": "Cimb"
        },
        {
            "value": 11,
            "display_name": "Gsb"
        }
    ];
    vm.selectedBanking = vm.bankChoices[0].display_name;
    vm.bankTypeChoices = [
                    {
                        "value": 0,
                        "display_name": "Visa"
                    },
                    {
                        "value": 1,
                        "display_name": "Mastercard"
                    }
                ];
    vm.selectedBankType = vm.bankTypeChoices[0].display_name;
    vm.addCardBoolean = false;

    vm.getAccountId = function (accountId) {
        vm.accountId = accountId;
    };

    vm.getBankAccounts = function () {
        $http.get(vm.url + '/api/bank_accounts/?account_owner=' + vm.accountId).then(
            function success(response) {
                vm.accounts = response.data;
            },
            function failure() {
                alert("Failed");
            }
        )
    };
    vm.getBankAccounts();
    vm.updateSelectedBank = function (index) {
        vm.selectBank = index;
    };

    vm.delBank = function (index) {
        vm.accounts.splice(index, 1);
    };
    vm.addCard = function () {
        vm.addCardBoolean = true;
    }
});