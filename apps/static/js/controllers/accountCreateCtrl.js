var app = angular.module('accountCreateApp', []);
app.controller('accountCreateCtrl', function ($scope, $http) {

    $scope.clickSignup = function () {
        var data = {
            user :{
                username: $scope.username,
                password: $scope.password
            },
            first_name: $scope.first_name,
            last_name: $scope.last_name,
            email: $scope.email,
            display_name: $scope.display_name,
            telephone: $scope.telephone
        };
        $http.post("http://localhost:8000/api/accounts/", data, {header: 'multipart/form-data'}).then(function (response) {
            console.log(response.data);
        });
    };
})
.config(function ($interpolateProvider) {
   $interpolateProvider.startSymbol('[[');
   $interpolateProvider.endSymbol(']]');
});