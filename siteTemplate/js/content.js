
d3.json("js/list_cn.json", function(error,data) {
	if (error) return console.warn(error);

	var items = [];
	for (var i = 0; i < data.list.length; i++) {
		items[i] = data.list[i].Name;
	}
	$('#sidebar ul').append('<li>' + items.join('</li><li>') + '</li>');
	$('#sidebar ul li:first-child').addClass('selected');

	$('#sidebar ul li').click(function(e) {
		var index = items.indexOf(e.target.innerHTML);

		$('#sidebar ul li').removeClass('selected');
		$('#sidebar ul li').eq(index).addClass('selected');
		$('.page-header small').html(e.target.innerHTML);
		$('.col-md-9 p').html(data.list[index].descr);
	});

});