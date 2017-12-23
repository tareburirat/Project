var app = angular.module('productCreateApp', []);
app.controller('productCreateCtrl', function ($scope, $http) {
    $scope.mama = 123;
    $scope.momo = "hello";
    $scope.product = {};
    $scope.prod = ['a', 'b'];
    $scope.prod_value = $scope.prod.slice();
    $scope.fTypes = ['Register', 'EMS', 'Kerry'];
    $scope.freight = $scope.fTypes[0];
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

        formData.append('freight', get_freight($scope.freight));
        debugger;
        var request = {
                    method: 'POST',
                    url: "/api/save_products/",
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

    };

    var get_freight = function (freight) {
        return $scope.fTypes.indexOf(freight);
    }
})
.config(function ($interpolateProvider, $httpProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
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
