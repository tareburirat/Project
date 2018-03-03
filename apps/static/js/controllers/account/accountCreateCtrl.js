app.controller('accountCreateCtrl', function ($scope, $http, $window, $rootScope) {
    var validUsername = '';
    var validDisplayName = '';

    $scope.panCardRegex = '/[A-Z]{5}\d{4}[A-Z]{1}/i';
    $scope.mama = $rootScope.url;

    $scope.clickSignup = function () {
        if ($scope.password !== $scope.passwordAgain ) {
            alert("รหัสผ่านไม่ตรงกัน");
            $scope.password = "";
            $scope.passwordAgain = "";
            return;
        } else if (validUsername === '' || validUsername !== $scope.username) {
            alert('กรุณาตรวจสอบ Username ก่อน');
            return;
        } else if (validDisplayName === '' || validDisplayName !== $scope.display_name) {
            alert('กรุณาตรวจสอบ Displayname ก่อน');
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
        $http.post($scope.mama + "/api/accounts/", data, {header: 'multipart/form-data'}).then(function (response) {
                console.log(response.data);
                alert('สมัครสมาชิกเรียบร้อย');
                $window.location.href = '/login';
            },
            function (response) {
                // console.log(response.data);
                alert("สมัครสมาชิกไม่สำเร็จ: " + response.data.message)

            });
    };

    $scope.checkUsername = function () {
        if (4 >= $scope.username.length || $scope.username.length >= 20) {
            alert('Username ต้องมากกว่า 4 และไม่ต่ำกว่า 20 ตัวอักษร');
            return;
        }
        $http.get($scope.mama + '/api/check_username/?username=' + $scope.username).then(
            function (response) {
                var data = response.data;
                var canUse = data.can_use;
                if (canUse) {
                    validUsername = $scope.username;
                    alert('สามารถใช้ Username นี้ได้');
                }else {
                    alert('ไม่สามารถใช้ Username นี้ได้');
                    $scope.username = '';
                }
            }
        )
    };

    $scope.checkDisplayname = function () {
        if (4 >= $scope.display_name.length || $scope.display_name.length >= 20) {
            alert('Username ต้องมากกว่า 4 และไม่ต่ำกว่า 20 ตัวอักษร');
            return;
        }
        $http.get($scope.mama + '/api/check_displayname/?display_name=' + $scope.display_name).then(
            function (response) {
                var data = response.data;
                var canUse = data.can_use;
                if (canUse) {
                    validDisplayName = $scope.display_name;
                    alert('สามารถใช้ Displayname นี้ได้');
                }else {
                    alert('ไม่สามารถใช้ Username นี้ได้');
                    $scope.display_name = '';
                }
            }
        )
    }
});