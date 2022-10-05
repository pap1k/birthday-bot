class PlaceObject:
    id : int
    title : str
    latitude : float
    longitude : float
    created : int
    icon : str
    country : str
    city: str

class GeoObject:
    type : str
    coordinates : list
    place: PlaceObject
    showmap : int

class MessageActionObject:
    type: str
    member_id:int
    text: str
    email: str
    photo: object

class Message:
    id                      : int  = None
    date                    : int = None
    peer_id                 : int = None
    from_id                 : int = None
    text                    : str = None
    random_id               : int = None
    ref                     : str = None
    ref_source              : str = None
    out                     : int = None
    attachments             : list = None
    important               : bool = None
    is_hidden               : bool = None
    geo                     : GeoObject = None
    payload                 : str = None
    keyboard                : dict = None
    fwd_messages            : list = None
    reply_message           : object = None
    action                  : MessageActionObject = None
    admin_author_id         : int = None
    conversation_message_id : int = None
    is_cropped              : int = None
    members_count           : int = None
    update_time             : int = None
    was_listened            : int = None
    pinned_at               : int = None
    message_tag             : str = None
    
    def __init__(self, id = None, date = None, peer_id = None, from_id = None, text = None, random_id = None, ref = None, ref_source = None, out = None, attachments = None, important = None, is_hidden = None, geo = None, payload = None, keyboard = None, fwd_messages = None, reply_message = None, action = None, admin_author_id = None, conversation_message_id = None, is_cropped = None, members_count = None, update_time = None, was_listened = None, pinned_at = None, message_tag = None) -> None:
        self.id = id
        self.date = date
        self.peer_id = peer_id
        self.from_id = from_id
        self.text = text
        self.random_id = random_id
        self.ref = ref
        self.ref_source = ref_source
        self.out = out
        self.attachments = attachments
        self.important = important
        self.is_hidden = is_hidden
        self.geo = geo
        self.payload = payload
        self.keyboard = keyboard
        self.fwd_messages = fwd_messages
        self.reply_message = reply_message
        self.action = action
        self.admin_author_id = admin_author_id
        self.conversation_message_id = conversation_message_id
        self.is_cropped = is_cropped
        self.members_count = members_count
        self.update_time = update_time
        self.was_listened = was_listened
        self.pinned_at = pinned_at
        self.message_tag = message_tag

class WallPost:
    id              : int = None
    owner_id        : int = None
    from_id         : int = None
    created_by      : int = None
    date            : int = None
    text            : str = None 
    reply_owner_id  : int = None
    reply_post_id   : int = None
    friends_only    : int = None
    comments        : object = None
    copyright       : object = None
    likes           : object = None
    reposts         : object = None
    views           : object = None
    post_type       : str = None
    post_source     : object = None
    attachments     : list = None
    geo             : GeoObject = None
    signer_id       : int = None
    copy_history    : list = None
    can_pin         : int = None
    can_delete      : int = None
    can_edit        : int = None
    is_pinned       : int = None
    marked_as_ads   : int = None
    is_favorite     : bool = None
    donut           : object = None
    postponed_id    : int = None
    
    def __init__(self, id = None, owner_id = None, from_id = None, created_by = None, date = None, text = None, reply_owner_id = None, reply_post_id = None, friends_only = None, comments = None, copyright = None, likes = None, reposts = None, views = None, post_type = None, post_source = None, attachments = None, geo = None, signer_id = None, copy_history = None, can_pin = None, can_delete = None, can_edit = None, is_pinned = None, marked_as_ads = None, is_favorite = None, donut = None, postponed_id = None):
        self.id = id
        self.owner_id = owner_id
        self.from_id = from_id
        self.created_by = created_by
        self.date = date
        self.text = text
        self.reply_owner_id = reply_owner_id
        self.reply_post_id = reply_post_id
        self.friends_only = friends_only
        self.comments = comments
        self.copyright = copyright
        self.likes = likes
        self.reposts = reposts
        self.views = views
        self.post_type = post_type
        self.post_source = post_source
        self.attachments = attachments
        self.geo = geo
        self.signer_id = signer_id
        self.copy_history = copy_history
        self.can_pin = can_pin
        self.can_delete = can_delete
        self.can_edit = can_edit
        self.is_pinned = is_pinned
        self.marked_as_ads = marked_as_ads
        self.is_favorite = is_favorite
        self.donut = donut
        self.postponed_id = postponed_id
