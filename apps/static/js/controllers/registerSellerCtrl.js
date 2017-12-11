var app = angular.module("app", []);
app.controller("registerSellerCtrl", function($scope, $http) {

    $scope.clicker = function () {
        var data = {
            username: $scope.username,
            password: $scope.password,
            first_name: $scope.first_name,
            last_name: $scope.last_name,
            display_name: $scope.display_name,
            telephone: $scope.telephone,
            address: $scope.address,
            country: $scope.country,
            city: $scope.city,
            zip_code: $scope.zip_code,
        };
        $http.post("http://localhost:8000/authenticate_user/", data).then(function (response) {
            console.log(response.data);
        });
    };

}).config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});