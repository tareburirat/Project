app.controller("passwordChangeCtrl", function ($scope, $http, $window) {
    $scope.mama = 123;
    $scope.panCardRegex = '/[A-Z]{5}\d{4}[A-Z]{1}/i';
    $scope.getUsername = function (username) {
        $scope.username = username;
    };

    $scope.passwordChange = function () {
        if ($scope.newPassword !== $scope.newPasswordAgain) {
            alert("New passwords do no match");
            $scope.newPassword = "";
            $scope.newPasswordAgain = "";
            return;
        }
        var data = {
            oldPassword: $scope.password,
            newPassword1: $scope.newPassword,
            newPassword2: $scope.newPasswordAgain
        };
        $http.post('http://localhost:8000/api/password_change/', data).then(
            function (response) {
                alert(response.data.message + " You changed your password and have to new login again.");

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
                alert("failed: " + response.data.message)
            }
        )
    }

});
app.directive('phone', function() {
    return {
        require: 'ngModel',
        link: function (scope, element, attr, ngModelCtrl) {
            function fromUser(text) {
                var transformedInput = text.replace(/[^0-9]/g, '');
                console.log(transformedInput);
                if(transformedInput !== text) {
                    ngModelCtrl.$setViewValue(transformedInput);
                    ngModelCtrl.$render();
                }
                return transformedInput;  // or return Number(transformedInput)
            }
            ngModelCtrl.$parsers.push(fromUser);
        }
    };
});

app.directive('username', function() {
    return {
        require: 'ngModel',
        link: function (scope, element, attr, ngModelCtrl) {
            function fromUser(text) {
                var transformedInput = text.replace(/[^A-Za-z0-9_-]/g, '');
                console.log(transformedInput);
                if(transformedInput !== text) {
                    ngModelCtrl.$setViewValue(transformedInput);
                    ngModelCtrl.$render();
                }
                return transformedInput;  // or return Number(transformedInput)
            }
            ngModelCtrl.$parsers.push(fromUser);
        }
    };
});
app.directive('isName', function() {
    return {
        require: 'ngModel',
        link: function (scope, element, attr, ngModelCtrl) {
            function fromUser(text) {
                var transformedInput = text.replace(/[^A-Za-z]/g, '');
                console.log(transformedInput);
                if(transformedInput !== text) {
                    ngModelCtrl.$setViewValue(transformedInput);
                    ngModelCtrl.$render();
                }
                return transformedInput;  // or return Number(transformedInput)
            }
            ngModelCtrl.$parsers.push(fromUser);
        }
    };
});
app.directive('isPassword', function() {
    return {
        require: 'ngModel',
        scope: {
            isPassword: '=isPassword'
        },
        link: function (scope, element, attr ,ngModelCtrl) {
            function fromUser(text) {
                var transformedInput = text.replace(/[^A-Za-z0-9]/g, '');
                console.log(transformedInput);
                if(transformedInput !== text) {
                    ngModelCtrl.$setViewValue(transformedInput);
                    ngModelCtrl.$render();
                }
                return transformedInput;  // or return Number(transformedInput)
            }
            scope.$watch('isPassword', function(a, b){
                element.attr('type', a ? 'text' : 'password')
            })
            ngModelCtrl.$parsers.push(fromUser);
        }
    }
});
