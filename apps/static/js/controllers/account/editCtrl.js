app.controller("accountEditCtrl", function ($scope, $http, $window, $rootScope) {
    $scope.mama = $rootScope.url;
    $scope.accountData = {};
    var url = "";

    $scope.getAccountInfo = function (accountId) {
        url = $scope.mama + '/api/accounts/' + accountId + '/';
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
                alert('แก้ไขข้อมูลสำเร็จ')
                $window.location.href = "/account/profile/"
            },
            function (reason) {
                alert('แก้ไขข้อมูลไม่สำเร็จ')
            }
        )
    }

});

