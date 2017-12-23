var app = angular.module('productCreateApp', []);
app.controller('productCreateCtrl', function ($scope, $http) {
    $scope.mama = 123;
    $scope.momo = "hello";
    $scope.product = {};
    $scope.prod = ['a', 'b'];
    $scope.prod_value = $scope.prod.slice();
    $scope.fTypes = ['register', 'ems', 'kerry'];
    var formData = new FormData();

    $scope.getTheFiles = function ($files) {
                angular.forEach($files, function (value, key) {
                    formData.append('images[]', value);
                });
            };

    $scope.clicky = function () {
        Object.keys($scope.product).forEach(function (k) {
            formData.append(k, $scope.product[k])
        });
        debugger;
        var request = {
                    method: 'POST',
                    url: "http://localhost:8000/api/save_products/",
                    data: formData,
                    headers: {
                        'Content-Type': undefined
                    }
                };
        $http(request).then(function () {
            alert('success');
        },
        function () {
            alert('failure');
        });

    }
})
.config(function ($interpolateProvider) {
   $interpolateProvider.startSymbol('[[');
   $interpolateProvider.endSymbol(']]');
})
.directive('ngFiles', ['$parse', function ($parse) {

            function fn_link(scope, element, attrs) {
                var onChange = $parse(attrs.ngFiles);
                element.on('change', function (event) {
                    onChange(scope, { $files: event.target.files });
                });
            };

            return {
                link: fn_link
            }
        } ]);