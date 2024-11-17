from enum import Enum
from typing import Optional, Union, List, Dict
from datetime import datetime


class Intensity(Enum):
    HIGH = "High"
    LOW = "Low"


class Banner:
    value: str
    intensity: Intensity
    backend_value: str

    def __init__(self, value: str, intensity: Intensity, backend_value: str) -> None:
        self.value = value
        self.intensity = intensity
        self.backend_value = backend_value


class BeanClass:
    small: str
    large: str

    def __init__(self, small: str, large: str) -> None:
        self.small = small
        self.large = large


class Lego:
    small: str
    large: str
    wide: Optional[str]

    def __init__(self, small: str, large: str, wide: Optional[str]) -> None:
        self.small = small
        self.large = large
        self.wide = wide


class Other:
    decal: Optional[str]
    coverart: Optional[str]

    def __init__(self, decal: Optional[str], coverart: Optional[str]) -> None:
        self.decal = decal
        self.coverart = coverart


class BrItemImages:
    small_icon: str
    icon: Optional[str]
    featured: Optional[str]
    lego: Optional[Lego]
    other: Optional[Other]
    bean: Optional[BeanClass]

    def __init__(self, small_icon: str, icon: Optional[str], featured: Optional[str], lego: Optional[Lego], other: Optional[Other], bean: Optional[BeanClass]) -> None:
        self.small_icon = small_icon
        self.icon = icon
        self.featured = featured
        self.lego = lego
        self.other = other
        self.bean = bean


class SeasonEnum(Enum):
    OG = "OG"
    X = "X"


class Introduction:
    chapter: int
    season: Union[SeasonEnum, int]
    text: str
    backend_value: int

    def __init__(self, chapter: int, season: Union[SeasonEnum, int], text: str, backend_value: int) -> None:
        self.chapter = chapter
        self.season = season
        self.text = text
        self.backend_value = backend_value


class Rarity:
    value: str
    display_value: str
    backend_value: str

    def __init__(self, value: str, display_value: str, backend_value: str) -> None:
        self.value = value
        self.display_value = display_value
        self.backend_value = backend_value


class BackendValue(Enum):
    CREATOR_COLLAB_SERIES = "CreatorCollabSeries"
    SERIES_TESLA = "Series_Tesla"


class Color(Enum):
    A2_ACB4_FF = "a2acb4ff"
    C2_CDD6_FF = "c2cdd6ff"
    D7_E3_EDFF = "d7e3edff"
    THE_000_F2_BFF = "000f2bff"
    THE_004_C71_FF = "004c71ff"
    THE_025253_FF = "025253ff"
    THE_222626_FF = "222626ff"
    THE_2_BC9_CAFF = "2bc9caff"
    THE_515_A62_FF = "515a62ff"
    THE_5_CF2_F3_FF = "5cf2f3ff"


class Value(Enum):
    ICON_SERIES = "Icon Series"
    TESLA_SERIES = "TESLA SERIES"


class Series:
    value: Value
    image: Optional[str]
    colors: List[Color]
    backend_value: BackendValue

    def __init__(self, value: Value, image: Optional[str], colors: List[Color], backend_value: BackendValue) -> None:
        self.value = value
        self.image = image
        self.colors = colors
        self.backend_value = backend_value


class Set:
    value: str
    text: str
    backend_value: str

    def __init__(self, value: str, text: str, backend_value: str) -> None:
        self.value = value
        self.text = text
        self.backend_value = backend_value


class Option:
    tag: str
    name: str
    image: str

    def __init__(self, tag: str, name: str, image: str) -> None:
        self.tag = tag
        self.name = name
        self.image = image


class Variant:
    channel: str
    type: str
    options: List[Option]

    def __init__(self, channel: str, type: str, options: List[Option]) -> None:
        self.channel = channel
        self.type = type
        self.options = options


class BrItem:
    id: str
    name: str
    description: str
    type: Rarity
    rarity: Rarity
    series: Optional[Series]
    set: Optional[Set]
    introduction: Optional[Introduction]
    images: BrItemImages
    showcase_video: Optional[str]
    added: datetime
    custom_exclusive_callout: Optional[str]
    variants: Optional[List[Variant]]
    built_in_emote_ids: Optional[List[str]]
    meta_tags: Optional[List[str]]
    dynamic_pak_id: Optional[int]

    def __init__(self, id: str, name: str, description: str, type: Rarity, rarity: Rarity, series: Optional[Series], set: Optional[Set], introduction: Optional[Introduction], images: BrItemImages, showcase_video: Optional[str], added: datetime, custom_exclusive_callout: Optional[str], variants: Optional[List[Variant]], built_in_emote_ids: Optional[List[str]], meta_tags: Optional[List[str]], dynamic_pak_id: Optional[int]) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.type = type
        self.rarity = rarity
        self.series = series
        self.set = set
        self.introduction = introduction
        self.images = images
        self.showcase_video = showcase_video
        self.added = added
        self.custom_exclusive_callout = custom_exclusive_callout
        self.variants = variants
        self.built_in_emote_ids = built_in_emote_ids
        self.meta_tags = meta_tags
        self.dynamic_pak_id = dynamic_pak_id


class Info(Enum):
    BUNDLE = "Bundle"


class Bundle:
    name: str
    info: Info
    image: str

    def __init__(self, name: str, info: Info, image: str) -> None:
        self.name = name
        self.info = info
        self.image = image


class Car:
    id: str
    vehicle_id: str
    name: str
    description: str
    type: Rarity
    rarity: Rarity
    images: BeanClass
    series: Series
    added: datetime

    def __init__(self, id: str, vehicle_id: str, name: str, description: str, type: Rarity, rarity: Rarity, images: BeanClass, series: Series, added: datetime) -> None:
        self.id = id
        self.vehicle_id = vehicle_id
        self.name = name
        self.description = description
        self.type = type
        self.rarity = rarity
        self.images = images
        self.series = series
        self.added = added


class EntryColors:
    color1: str
    color2: Optional[str]
    color3: str
    text_background_color: str

    def __init__(self, color1: str, color2: Optional[str], color3: str, text_background_color: str) -> None:
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.text_background_color = text_background_color


class Instrument:
    id: str
    name: str
    description: str
    type: Rarity
    rarity: Rarity
    images: BeanClass
    series: Optional[Series]
    added: datetime

    def __init__(self, id: str, name: str, description: str, type: Rarity, rarity: Rarity, images: BeanClass, series: Optional[Series], added: datetime) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.type = type
        self.rarity = rarity
        self.images = images
        self.series = series
        self.added = added


class Category(Enum):
    ROYALE_ORIGINALS = "Royale Originals"
    SPOTLIGHT = "Spotlight"
    START_YOUR_ENGINES = "Start Your Engines"
    TAKE_YOUR_STAGE = "Take Your Stage"


class DisplayType(Enum):
    BILLBOARD = "billboard"
    EXPANDABLE_LIST = "expandableList"
    TILE_GRID = "tileGrid"


class LayoutID(Enum):
    CYBERTRUCK = "Cybertruck"
    EMINEM = "Eminem"
    FORTNITE_FLOW = "FortniteFlow"
    ICE_SPICE = "IceSpice"
    JAM_TRACKS1117 = "JamTracks1117"
    LADY_GAGA = "LadyGaga"
    RELOAD = "Reload"
    SIGNATURE_STYLE1117 = "SignatureStyle1117"
    SNOOP_DOGG = "SnoopDogg"
    SPARKS_INSTRUMENTS34 = "SparksInstruments34"
    TMNT = "TMNT"


class Name(Enum):
    EMINEM = "Eminem"
    FORTNITE_FLOW = "Fortnite Flow"
    GEAR_FOR_FESTIVAL = "Gear For Festival"
    ICE_SPICE = "Ice Spice"
    JAM_TRACKS = "Jam Tracks"
    LADY_GAGA = "Lady Gaga"
    RELOAD_SQUADS = "Reload Squads"
    SIGNATURE_STYLE = "Signature Style"
    SNOOP_DOGG = "Snoop Dogg"
    TEENAGE_MUTANT_NINJA_TURTLES = "Teenage Mutant Ninja Turtles"
    TESLA = "Tesla"


class ShowIneligibleOffers(Enum):
    ALWAYS = "always"


class Metadatum:
    key: str
    value: str

    def __init__(self, key: str, value: str) -> None:
        self.key = key
        self.value = value


class Layout:
    id: LayoutID
    name: Name
    category: Category
    index: int
    rank: int
    show_ineligible_offers: ShowIneligibleOffers
    use_wide_preview: bool
    display_type: DisplayType
    texture_metadata: Optional[List[Metadatum]]
    string_metadata: Optional[List[Metadatum]]
    text_metadata: Optional[List[Metadatum]]

    def __init__(self, id: LayoutID, name: Name, category: Category, index: int, rank: int, show_ineligible_offers: ShowIneligibleOffers, use_wide_preview: bool, display_type: DisplayType, texture_metadata: Optional[List[Metadatum]], string_metadata: Optional[List[Metadatum]], text_metadata: Optional[List[Metadatum]]) -> None:
        self.id = id
        self.name = name
        self.category = category
        self.index = index
        self.rank = rank
        self.show_ineligible_offers = show_ineligible_offers
        self.use_wide_preview = use_wide_preview
        self.display_type = display_type
        self.texture_metadata = texture_metadata
        self.string_metadata = string_metadata
        self.text_metadata = text_metadata


class BackgroundInnerGradient(Enum):
    F0_FFEEFF = "f0ffeeff"
    THE_00_D15_AFF = "00d15aff"


class BackgroundOuterGradient(Enum):
    F0_FEEEFF = "f0feeeff"
    THE_004433_FF = "004433ff"


class PatternInnerGradient(Enum):
    CFDCCEFF = "cfdcceff"
    THE_00_F075_FF = "00f075ff"


class PatternOuterGradient(Enum):
    A9_B3_A8_FF = "a9b3a8ff"
    THE_003_F25_FF = "003f25ff"


class SheenColor(Enum):
    THE_1_FBF60_FF = "1fbf60ff"


class MaterialInstanceColors:
    background_color_a: Optional[str]
    background_color_b: Optional[str]
    background_inner_gradient: Optional[BackgroundInnerGradient]
    background_outer_gradient: Optional[BackgroundOuterGradient]
    pattern_inner_gradient: Optional[PatternInnerGradient]
    pattern_outer_gradient: Optional[PatternOuterGradient]
    sheen_color: Optional[SheenColor]
    fall_off_color: Optional[str]
    background_color_1: Optional[str]
    floor_radial_angle: Optional[str]
    floor_radial_offset: Optional[str]

    def __init__(self, background_color_a: Optional[str], background_color_b: Optional[str], background_inner_gradient: Optional[BackgroundInnerGradient], background_outer_gradient: Optional[BackgroundOuterGradient], pattern_inner_gradient: Optional[PatternInnerGradient], pattern_outer_gradient: Optional[PatternOuterGradient], sheen_color: Optional[SheenColor], fall_off_color: Optional[str], background_color_1: Optional[str], floor_radial_angle: Optional[str], floor_radial_offset: Optional[str]) -> None:
        self.background_color_a = background_color_a
        self.background_color_b = background_color_b
        self.background_inner_gradient = background_inner_gradient
        self.background_outer_gradient = background_outer_gradient
        self.pattern_inner_gradient = pattern_inner_gradient
        self.pattern_outer_gradient = pattern_outer_gradient
        self.sheen_color = sheen_color
        self.fall_off_color = fall_off_color
        self.background_color_1 = background_color_1
        self.floor_radial_angle = floor_radial_angle
        self.floor_radial_offset = floor_radial_offset


class MaterialInstanceImages:
    offer_image: Optional[str]
    texture: Optional[str]
    background: str
    image_background: Optional[str]
    car_texture: Optional[str]
    car_util: Optional[str]
    item_stack_texture: Optional[str]

    def __init__(self, offer_image: Optional[str], texture: Optional[str], background: str, image_background: Optional[str], car_texture: Optional[str], car_util: Optional[str], item_stack_texture: Optional[str]) -> None:
        self.offer_image = offer_image
        self.texture = texture
        self.background = background
        self.image_background = image_background
        self.car_texture = car_texture
        self.car_util = car_util
        self.item_stack_texture = item_stack_texture


class PrimaryMode(Enum):
    E_COSMETIC_COMPATIBLE_MODE_LEGACY_MAX = "ECosmeticCompatibleModeLegacy::MAX"


class ProductTag(Enum):
    PRODUCT_BR = "Product.BR"
    PRODUCT_DEL_MAR = "Product.DelMar"
    PRODUCT_JUNO = "Product.Juno"
    PRODUCT_SPARKS = "Product.Sparks"


class MaterialInstance:
    id: str
    primary_mode: PrimaryMode
    product_tag: ProductTag
    images: MaterialInstanceImages
    colors: MaterialInstanceColors
    scalings: Dict[str, float]
    flags: Optional[Dict[str, bool]]

    def __init__(self, id: str, primary_mode: PrimaryMode, product_tag: ProductTag, images: MaterialInstanceImages, colors: MaterialInstanceColors, scalings: Dict[str, float], flags: Optional[Dict[str, bool]]) -> None:
        self.id = id
        self.primary_mode = primary_mode
        self.product_tag = product_tag
        self.images = images
        self.colors = colors
        self.scalings = scalings
        self.flags = flags


class RenderImage:
    product_tag: ProductTag
    file_name: str
    image: str

    def __init__(self, product_tag: ProductTag, file_name: str, image: str) -> None:
        self.product_tag = product_tag
        self.file_name = file_name
        self.image = image


class NewDisplayAsset:
    id: str
    cosmetic_id: Optional[str]
    material_instances: List[MaterialInstance]
    render_images: List[RenderImage]

    def __init__(self, id: str, cosmetic_id: Optional[str], material_instances: List[MaterialInstance], render_images: List[RenderImage]) -> None:
        self.id = id
        self.cosmetic_id = cosmetic_id
        self.material_instances = material_instances
        self.render_images = render_images


class OfferTagID(Enum):
    BOUNDLESSDISABLEDCOMP = "boundlessdisabledcomp"
    FUTURE = "future"
    HEAVYROAR = "heavyroar"
    HEAVYROARBUNDLE = "heavyroarbundle"
    KITTYWARRIORINSPECT = "kittywarriorinspect"
    PROMODESC102 = "promodesc102"
    QUIETPEANUTS = "quietpeanuts"
    REACTIVETVBACKBLING = "reactivetvbackbling"
    SMOKE = "smoke"
    SPARKSJAMLOOP = "sparksjamloop"
    STYLES = "styles"


class OfferTag:
    id: OfferTagID
    text: str

    def __init__(self, id: OfferTagID, text: str) -> None:
        self.id = id
        self.text = text


class TileSize(Enum):
    SIZE_1__X_1 = "Size_1_x_1"
    SIZE_2__X_1 = "Size_2_x_1"
    SIZE_3__X_1 = "Size_3_x_1"
    SIZE_4__X_1 = "Size_4_x_1"


class Difficulty:
    vocals: int
    guitar: int
    bass: int
    plastic_bass: int
    drums: int
    plastic_drums: int

    def __init__(self, vocals: int, guitar: int, bass: int, plastic_bass: int, drums: int, plastic_drums: int) -> None:
        self.vocals = vocals
        self.guitar = guitar
        self.bass = bass
        self.plastic_bass = plastic_bass
        self.drums = drums
        self.plastic_drums = plastic_drums


class Genre(Enum):
    DANCE_ELECTRONIC = "DanceElectronic"
    POP = "Pop"
    RAP_HIP_HOP = "RapHipHop"
    RN_B = "RnB"
    ROCK = "Rock"


class Track:
    id: str
    dev_name: str
    title: str
    artist: str
    album: Optional[str]
    release_year: int
    bpm: int
    duration: int
    difficulty: Difficulty
    genres: Optional[List[Genre]]
    album_art: str
    added: datetime

    def __init__(self, id: str, dev_name: str, title: str, artist: str, album: Optional[str], release_year: int, bpm: int, duration: int, difficulty: Difficulty, genres: Optional[List[Genre]], album_art: str, added: datetime) -> None:
        self.id = id
        self.dev_name = dev_name
        self.title = title
        self.artist = artist
        self.album = album
        self.release_year = release_year
        self.bpm = bpm
        self.duration = duration
        self.difficulty = difficulty
        self.genres = genres
        self.album_art = album_art
        self.added = added


class Entry:
    regular_price: int
    final_price: int
    dev_name: str
    offer_id: str
    in_date: datetime
    out_date: datetime
    giftable: bool
    refundable: bool
    sort_priority: int
    layout_id: str
    layout: Layout
    colors: Optional[EntryColors]
    tile_size: TileSize
    new_display_asset_path: str
    new_display_asset: Optional[NewDisplayAsset]
    br_items: Optional[List[BrItem]]
    offer_tag: Optional[OfferTag]
    tracks: Optional[List[Track]]
    bundle: Optional[Bundle]
    banner: Optional[Banner]
    display_asset_path: Optional[str]
    instruments: Optional[List[Instrument]]
    cars: Optional[List[Car]]

    def __init__(self, regular_price: int, final_price: int, dev_name: str, offer_id: str, in_date: datetime, out_date: datetime, giftable: bool, refundable: bool, sort_priority: int, layout_id: str, layout: Layout, colors: Optional[EntryColors], tile_size: TileSize, new_display_asset_path: str, new_display_asset: Optional[NewDisplayAsset], br_items: Optional[List[BrItem]], offer_tag: Optional[OfferTag], tracks: Optional[List[Track]], bundle: Optional[Bundle], banner: Optional[Banner], display_asset_path: Optional[str], instruments: Optional[List[Instrument]], cars: Optional[List[Car]]) -> None:
        self.regular_price = regular_price
        self.final_price = final_price
        self.dev_name = dev_name
        self.offer_id = offer_id
        self.in_date = in_date
        self.out_date = out_date
        self.giftable = giftable
        self.refundable = refundable
        self.sort_priority = sort_priority
        self.layout_id = layout_id
        self.layout = layout
        self.colors = colors
        self.tile_size = tile_size
        self.new_display_asset_path = new_display_asset_path
        self.new_display_asset = new_display_asset
        self.br_items = br_items
        self.offer_tag = offer_tag
        self.tracks = tracks
        self.bundle = bundle
        self.banner = banner
        self.display_asset_path = display_asset_path
        self.instruments = instruments
        self.cars = cars


class Data:
    hash: str
    date: datetime
    vbuck_icon: str
    entries: List[Entry]

    def __init__(self, hash: str, date: datetime, vbuck_icon: str, entries: List[Entry]) -> None:
        self.hash = hash
        self.date = date
        self.vbuck_icon = vbuck_icon
        self.entries = entries


class CreditsResponse:
    status: int
    data: Data

    def __init__(self, status: int, data: Data) -> None:
        self.status = status
        self.data = data
