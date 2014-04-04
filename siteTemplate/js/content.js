
d3.json("list_cn.json", function(error,data) {
	if (error) return console.warn(error);
	console.log(data);
	console.log(data.length)
});