app.controller("passwordChangeCtrl", function ($scope, $http, $window, $rootScope) {
    $scope.mama = $rootScope.url;
    $scope.panCardRegex = '/[A-Z]{5}\d{4}[A-Z]{1}/i';
    $scope.getUsername = function (username) {
        $scope.username = username;
    };

    $scope.passwordChange = function () {
        if ($scope.newPassword !== $scope.newPasswordAgain) {
            alert("รหัสผ่านไม่ตรงกัน");
            $scope.newPassword = "";
            $scope.newPasswordAgain = "";
            return;
        }
        var data = {
            oldPassword: $scope.password,
            newPassword1: $scope.newPassword,
            newPassword2: $scope.newPasswordAgain
        };
        $http.post($scope.mama + '/api/password_change/', data).then(
            function (response) {
                alert(response.data.message + "เปลี่ยนรหัสผ่านสำเร็จ โปรดเข้าสู่ระบบอีกครั้ง");

                // var user_data = {
                //     username: $scope.username,
                //     password: $scope.newPassword
                // };
                //
                // $http.post("http://localhost:8000/authenticate_user/", user_data).then(function (response) {
                //     $window.location.href = '/';
                // });

                $window.location.href = '/login/';
            },
            function (response) {
                alert("เปลี่ยนรหัสผ่านไม่สำเร็จ: " + response.data.message)
            }
        )
    }
});