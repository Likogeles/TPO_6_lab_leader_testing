class Locator(object):
    # Leader login
    open_login_window_btn = "//div[@data-qa='loginOpenBtn']"
    email_field = "//input[@autocomplete='username']"
    password_field = "//input[@autocomplete='password']"
    log_in_button = "//button[@data-qa='loginSubmitBtn']"
    profile_icon = "//div[@class='_3d9fHqIpGHGZ el-popover__reference']"

    # Leader profile
    change_password_btn = '//button[@class="app-button app-button--default app-button--lg"]'
    old_password_field = '//input[@autocomplete="old-password"]'
    new_password_field = '//input[@autocomplete="new-password"]'
    commit_change_password_btn = '//button[@class="app-button app-button--primary app-button--lg G1JlLFJ2O6yX"]'
    success_change_password = '//div[@role="alert"]'

    # Events
    name_input_field = '//input[@class="events-index__header-search-input"]'
    card = '//div[@class="app-card-event PVduZCM7jrTd"]'
    remove_city_events_filter_btn = '//span[@class="app-filter__arrow-container app-filter__arrow-container--action"]'

    # BoilPoints
    remove_city_boil_points_filter_btn = '//span[@class="app-filter__arrow-container app-filter__arrow-container--action"]'
    all_cities_btn = '//div[@class="app-filter _1yEWYuYb0p8E"]/span'
    search_city_field = '//input[@class="app-input__inner"]'
    search_city_card = '//div[@class="app-filter-item is-selected is-focused"]'
    download_btn = '//button[@class="app-button app-button--default app-button--sm app-button--icon"]'

    # Users
    all_filters_users_btn = '//div[@class="app-filter-tag__reference el-popover__reference"]'
    filter_tags = '//span[@class="app-tag app-tag--clickable app-tag--round"]'
    close_filter_tags_btn = '//button[@class="app-button close app-button--default app-button--sm"]'
    leader_cards = '//div[@class="search-user"]'



