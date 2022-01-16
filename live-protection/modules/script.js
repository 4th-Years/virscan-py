popup=document.getElementById("popup")
API_KEY='62275244469f19bb4568943a98fe16cf1d8063e145407bb577ddee3b1be717db'

function analyse(url){
	const options = {
		method: 'POST',
		headers: {
			Accept: 'application/json',
			'x-apikey': API_KEY,
			'Content-Type': 'application/x-www-form-urlencoded'
		},
		body: new URLSearchParams({url: url})
	};

	return fetch('https://www.virustotal.com/api/v3/urls', options)
	.then(response => response.json())
	.then(response => {
			id = response['data']['id']
			console.log(id)
			return id
	})
	.catch(err => console.error(err));
}

function get_badness_score(stats){
/*
 * get BAD-ness score from stats, where stats is an obejct like
      "stats": {
        "harmless": 71,
        "malicious": 14,
        "suspicious": 0,
        "undetected": 9,
        "timeout": 0
      },
*/
	total = stats["malicious"] + stats["suspicious"] + stats["harmless"]
	if (total < 1) {
		return 0
	}
	bad = stats["malicious"] + stats["suspicious"]
	return 100.0 * bad / total
}

function get_bad_categories(results){
	/*
	 *
        "PhishLabs": {
          "category": "malicious",
          "result": "phishing",
          "method": "blacklist",
          "engine_name": "PhishLabs"
        },
	*/
	categories = new Set()
	console.log("Result is ")
	console.log(results)
	for (vendor in results){
		result = results[vendor]
		if (result["category"] == "malicious" || result["category"] == "suspicious"){
			categories.add(result["result"])
		}
	}

	return Array.from(categories)
}

function result_template(color, text, image){
	dom = `
	<div class="center result" style="border-color:${color}">
		<img src="${image}" alt="status" class="result"/><br/>
		${text}
	</div>
	`
	return dom
}

function fetch_and_update_dom(id){
	const options = {
	  method: 'GET',
	  headers: {
		Accept: 'application/json',
		'x-apikey': API_KEY
	  }
	};

	fetch(`https://www.virustotal.com/api/v3/analyses/${id}`, options)
	  .then(response => response.json())
	  .then(response => {
			  console.log(response)
			  url = response["meta"]["url_info"]["url"]
			  stats = response["data"]["attributes"]["stats"]
			  results = response["data"]["attributes"]["results"]
			  score = Math.round(get_badness_score(stats))

			  if (score > 0){ // unsafe
				  categories = get_bad_categories(results)
				  color = "red"
				  text = `The website is infected !<br/>Infection: ${score}%<br/>
				  Infection type: ${categories.join(", ")}`
				  image = "images/cross.png"
			  }
			  else {
				  color = "green"
				  text = "Website is safe to visit"
				  image = "images/tick.png"
			  }
			  popup.innerHTML = result_template(color, text, image)
	  })
	  .catch(err => console.error(err));
}

browser.tabs.query({currentWindow: true, active: true})
.then(async (tabs) => {
		/* debug values
		id = 'u-897b630ff72981ff93f8ab8ae3ecabdf8388f74a5ee4a7f212b368ea6501efa6-1642339342'
		popup.innerHTML = result_template("red", "ok", "images/cross.png")
		 */
		tab = tabs[0]
		popup.innerHTML = popup.innerHTML.replace("{{url}}", tab.url)
		id = await analyse(tab.url)
		setTimeout(x => fetch_and_update_dom(id), 5000)
})
.catch(err => console.log(err))
