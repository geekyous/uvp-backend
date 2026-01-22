from app.models.request_respones import QueryResourcesVO
from app.models.resources_model import DeviceResource


def device_resource_to_vo(
        r: DeviceResource,
        *,
        children_count: int | None = None,
        child_nodes: list[QueryResourcesVO] | None = None
) -> QueryResourcesVO:
    return QueryResourcesVO(
        id=r.id,
        text=r.text,
        devShortName=r.dev_short_name,
        pNotes=r.p_notes,
        pCode=r.p_code,
        url=r.url,
        openType=r.open_type,
        pid=r.pid,
        path=r.path,
        type=r.type,
        isGroup=r.is_group,
        isAvailable=r.is_available,
        order=r.order,
        hasChildren=children_count > 0 if children_count is not None else r.has_children,
        status=r.status,
        isOuternet=r.is_outernet,
        sDecodeTag=r.s_decode_tag,
        devCode=r.dev_code,
        devType=r.dev_type,
        lng=r.lng,
        lat=r.lat,
        childrenCount=children_count if children_count is not None else r.children_count,
        gisPeerCode=r.gis_peer_code,
        childNodes=child_nodes or [],
        sysInfoCode=r.sys_info_code,
        dvrCode=r.dvr_code,
        isCheck=r.is_check,
        fontTypeCode=r.font_type_code,
        peerId=r.peer_id,
        audio=r.audio,
    )
