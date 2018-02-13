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
                var transformedInput = text.replace(/[^A-Za-zก-ฮ]/g, '');
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
