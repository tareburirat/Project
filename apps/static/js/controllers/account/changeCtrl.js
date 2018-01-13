var app = angular.module("app", []);
    app.controller("passwordChangeCtrl", function ($scope, $http, $window) {
    $scope.mama = 123;

    $scope.passwordChange = function () {
        if ($scope.newPassword !== $scope.newPasswordAgain) {
            alert("New passwords do no match");
            $scope.newPassword = "";
            $scope.newPasswordAgain = "";
            return;
        }
        var data = {
            oldPassword : $scope.password,
            newPassword1 : $scope.newPassword,
            newPassword2 : $scope.newPasswordAgain
        };
        $http.post('http://localhost:8000/api/password_change/',data).then(
            function (response) {
                alert(response.data.message);
                $window.location.href = '/account/profile/';
            },
            function (response) {
                alert("failed: " + response.data.message)
            }
        )

    }

}).config(function($interpolateProvider, $httpProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});
