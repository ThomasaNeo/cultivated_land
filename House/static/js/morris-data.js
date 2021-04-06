$(function() {
    let lg05 = $("#morris-donut-chart").attr('lg05')
    let lg06 = $("#morris-donut-chart").attr('lg06')
    let lt06 = $("#morris-donut-chart").attr('lt06')
    Morris.Donut({
        element: 'morris-donut-chart',
        data: [{
            label: "住宅类",
            value: lg05
        }, {
            label: "产业类",
            value: lg06
        }, {
            label: "公共服务类",
            value: lt06
        }],
        resize: true
    });


});
