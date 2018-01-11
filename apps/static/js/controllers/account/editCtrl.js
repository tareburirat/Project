var app = angular.module("app", []);
app.controller("accountEditCtrl", function ($scope, $http) {
    $scope.mama = 123;
    $scope.accountData = {};
    var url = "";

    $scope.getAccountInfo = function (accountId) {
        url = 'http://localhost:8000/api/accounts/' + accountId + '/';
        $http.get(url).then(
            function (response) {
                $scope.accountData = response.data;
            },
            function (response) {
                alert("failed")
            }
        )
    };

    $scope.saveProduct = function () {
        var data = {
            first_name: $scope.accountData.first_name,
            last_name: $scope.accountData.last_name,
            email: $scope.accountData.email,
            display_name: $scope.accountData.display_name,
            phone: $scope.accountData.phone
        };
        $http.put(url, data).then(
            function (response) {
                alert('success')
            },
            function (reason) {
                alert('failed')
            }
        )
    }

})
.config(function($interpolateProvider, $httpProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});
