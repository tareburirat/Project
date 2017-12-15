var app = angular.module("app", []);
app.controller("logInCtrl", function($scope, $http) {
    $scope.mama = 123;
    $scope.userLoggedIn = false;

    $scope.clicker = function () {
        console.log("Entered!!!");
        var data = {
            username: $scope.username,
            password: $scope.password
        };
        $http.post("http://localhost:8000/authenticate_user/", data).then(function (response) {
            console.log(response.data);
            $scope.userLoggedIn = true;
        });

    };


}).config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});