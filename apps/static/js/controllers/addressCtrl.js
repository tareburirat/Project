var app = angular.module("app", []);
    app.controller("addressCtrl", function ($scope, $http, $window) {
        $scope.mama = 123;

            $scope.getAddress = function () {
        var data = {
            address: $scope.address,
            sub_district: $scope.sub_district,
            district: $scope.district,
            province: $scope.province,
            zip_code: $scope.zip_code,
        };
         $http.post('http://localhost:8000/api/address_buyer/',data).then(
            function (response) {
                alert(response.data);
                $window.location.href = '/address_buyer/';
            },
            function (response) {
                alert("failed: " + response.data)
            }
        )
    }

})

.config(function ($interpolateProvider) {
   $interpolateProvider.startSymbol('[[');
   $interpolateProvider.endSymbol(']]');
});