var app = angular.module('accountCreateApp', []);
app.controller('accountCreateCtrl', function ($scope, $http, $window) {

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
            phone: $scope.phone
        };
        $http.post("http://localhost:8000/api/accounts/", data, {header: 'multipart/form-data'}).then(function (response) {
            console.log(response.data);
            alert('success!!');
            $window.location.href = '/login';
        },
            function (response) {
                console.log(response.data);
                alert('failed!!');
                $scope.username = '';
                $scope.password = '';
                $scope.first_name = '';
                $scope.last_name = '';
                $scope.email = '';
                $scope.display_name = '';
                $scope.phone = '';
            });
    };
})
.config(function ($interpolateProvider) {
   $interpolateProvider.startSymbol('[[');
   $interpolateProvider.endSymbol(']]');
});