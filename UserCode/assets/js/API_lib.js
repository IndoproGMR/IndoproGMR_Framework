class API_lib{
  constructor(baseURL){
    if (!baseURL.endsWith('/')) {
      baseURL += '/';
    }
    this.baseURL = baseURL
    console.log(this.baseURL)
  }

  async get(endpoint,param={}){
    const url = new URL(endpoint,this.baseURL);
    Object.keys(param).forEach((key)=>
      url.searchParams.append(key,param[key])
    );

    try {
      const respond = await fetch(url.toString());
      if (!respond.ok) {
        throw new Error(`http Error: ${respond.status}`);
      }
  
      const data = await respond.json();
      //console.log(data);
      return data
    } catch (error) {
      throw new Error(`Failed to fetch data: ${error.message}`);
    }
  }
  async post(endpoint,data={}){
    //const url = newURL(endpoint);
  }




}
