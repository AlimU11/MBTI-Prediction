from enum import auto

from .StrEnum import StrEnum


class IdHolder(StrEnum):
    UNDEFINED = auto()

    # Pages
    index = auto()
    types = auto()
    train_results = auto()

    # shared callback dispatcher for index and types pages
    index_type_callback_dispatcher = auto()

    # index

    input_container = auto()
    input_switch = auto()
    input_profile = auto()
    input_area = auto()
    input_button = auto()
    input_profile_wrapper = auto()
    input_show_tokens_button = auto()
    input_tokens_toast = auto()

    prediction_container = auto()
    personality_type_container = auto()
    personality_graph = auto()
    profile_img = auto()
    profile_username = auto()
    profile_container = auto()

    famous_people_container = auto()
    type_description = auto()
    strengths_container = auto()
    weaknesses_container = auto()
    ideal_partners_container = auto()
    careers_container = auto()
    interests_container = auto()

    # dashboard
    dashboard_callback_dispatcher = auto()

    types_distribution_graph = auto()
    indicators_distribution_graph = auto()
    feature_heatmap_graph = auto()
    table_container = auto()
    feature_importance_graph = auto()
    roc_auc_graph = auto()

    # types
    input_dropdown = auto()
