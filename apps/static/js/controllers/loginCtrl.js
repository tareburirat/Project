app.controller("logInCtrl", function($scope, $http, $window) {
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
            alert('success!!');
            $window.location.href = '/';
        },
            function (response) {
                console.log(response.data);
                alert('failed');
                $scope.username = '';
                $scope.password = '';
            });

    };


});