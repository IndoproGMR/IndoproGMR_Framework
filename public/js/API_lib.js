class API_lib {
    constructor(baseURL) {
        this.baseURL = baseURL;
    }

    async get(endpoint, params = {}) {
        const url = new URL(endpoint, this.baseURL);
        Object.keys(params).forEach((key) =>
            url.searchParams.append(key, params[key])
        );

        try {
            const response = await fetch(url.toString());
            if (!response.ok) {
                throw new Error(`HTTP Error: ${response.status}`);
            }
            const data = await response.json();
            return data;
        } catch (error) {
            throw new Error(`Failed to fetch data: ${error.message}`);
        }
    }

    async post(endpoint, data = {}) {
        const url = new URL(endpoint, this.baseURL);

        try {
            const response = await fetch(url.toString(), {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
            });

            if (!response.ok) {
                throw new Error(`HTTP Error: ${response.status}`);
            }

            const responseData = await response.json();
            return responseData;
        } catch (error) {
            throw new Error(`Failed to fetch data: ${error.message}`);
        }
    }
}
