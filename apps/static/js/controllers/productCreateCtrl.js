var app = angular.module('productCreateApp', []);
app.controller('productCreateCtrl', function ($scope, $http) {
    $scope.mama = 123;
    $scope.product = {};
    $scope.fTypes = ['Register', 'EMS', 'Kerry'];
    $scope.freight = $scope.fTypes[0];
    $scope.categories = [];
    $scope.selectedCategory = {};
    $scope.properties = [];
    var formData = new FormData();

    $scope.getAccountId = function (accountId) {
        $scope.accountId = accountId;
    };

    $scope.getTheFiles = function ($files) {
                angular.forEach($files, function (value, key) {
                    formData.append('images[]', value);
                });
            };

    $scope.submitProduct = function () {
        // get product details
        Object.keys($scope.product).forEach(function (k) {
            formData.append(k, $scope.product[k])
        });

        // get category
        formData.append('category_id', $scope.selectedCategory.id);

        // get freight option
        formData.append('freight', get_freight($scope.freight));
        formData.append('seller_id', $scope.accountId);

        // get property values
        angular.forEach($scope.properties, function (property) {
            formData.append('propertyValue[]', property.value);
            formData.append('propertyId[]', property.id);
        });

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
    };

    var categories_request = {
        method: 'GET',
        url: '/api/categories/?category_type=0',
    };
    $http(categories_request).then(function (response) {
        $scope.categories = response.data;
        $scope.selectedCategory = $scope.categories[0];
        $scope.getProperties($scope.selectedCategory.id);
    }, function (response) {
        alert(response);
    });

    $scope.getProperties = function (catId) {
        var getPropertyRequest = {
            method: 'GET',
            url: '/api/properties/?category_id=' + catId
        };
        $http(getPropertyRequest).then(function (response) {
             $scope.properties = response.data;
        })
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
    }

    return {
        link: fn_link
    }
} ]);
