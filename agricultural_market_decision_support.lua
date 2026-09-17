math.randomseed(os.time())

-- A. Model each market as a coroutine yielding changing prices

local function create_market(start_price)
    return coroutine.create(function()
        local current_price = start_price

        while true do
            -- Generate a fictional price fluctuation
            local change = math.random(-200, 300)

            current_price = current_price + change

            coroutine.yield(current_price)
        end
    end)
end

-- B. Maintain price history separately for every market

local markets = {
    { name = "Kitale",  co = create_market(4200), history = {} },
    { name = "Eldoret", co = create_market(4350), history = {} },
    { name = "Nakuru",  co = create_market(4100), history = {} },
    { name = "Kisumu",  co = create_market(4300), history = {} },
    { name = "Nairobi", co = create_market(4250), history = {} }
}

local round = 1
local sale_made = false

-- Central Scheduler Loop

while not sale_made do
    print("\n--- Round " .. round .. " ---")

    for _, market in ipairs(markets) do
        -- Resume coroutine to fetch the newest price
        local status, latest_price = coroutine.resume(market.co)

        if status then
            table.insert(market.history, latest_price)

            print(market.name .. " current price: KSh " .. latest_price)

            -- C. Determine when the selling condition is satisfied

            local len = #market.history

            if len >= 3 then
                local p1 = market.history[len - 2]
                local p2 = market.history[len - 1]
                local p3 = market.history[len]

                -- Check: Exceeds KSh 4,500 AND increased in two consecutive rounds

                if p3 > 4500 and p3 > p2 and p2 > p1 then
                    print(
                        "\n>>> SUCCESS: "
                            .. market.name
                            .. " satisfies conditions at KSh "
                            .. p3
                            .. "!"
                    )

                    sale_made = true

                    -- D. Stop unnecessary coroutine execution
                    break
                end
            end
        else
            print("Error resuming " .. market.name)
        end
    end

    -- Safety mechanism to prevent infinite loops during testing

    if round > 50 then
        print("\nNo suitable market found after 50 rounds.")
        break
    end

    round = round + 1
end