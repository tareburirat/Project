app.controller('accountCreateCtrl', function ($scope, $http, $window) {
    $scope.panCardRegex = '/[A-Z]{5}\d{4}[A-Z]{1}/i';

    $scope.clickSignup = function () {
        if ($scope.password !== $scope.passwordAgain) {
            alert("รหัสผ่านไม่ตรงกัน");
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
                alert('สมัครสมาชิคเรียบร้อย');
                $window.location.href = '/login';
            },
            function (response) {
                // console.log(response.data);
                alert("สมัครสมาชิคไม่สำเร็จ: " + response.data.message)

            });
    };
});