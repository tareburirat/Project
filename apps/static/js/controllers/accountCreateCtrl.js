app.controller('accountCreateCtrl', function ($scope, $http, $window) {

    $scope.clickSignup = function () {
        if ($scope.password !== $scope.passwordAgain) {
            alert("Passwords do no match");
            $scope.password = "";
            $scope.passwordAgain = "";
            return;
        }
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
                // console.log(response.data);
                alert("failed: " + response.data.message)

            });
    };
});